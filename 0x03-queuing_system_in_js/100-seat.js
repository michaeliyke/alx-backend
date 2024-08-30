const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

const reserveSeat = async (number) => {
  const setAsync = promisify(client.set).bind(client);
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.get).bind(client);
  const seats = await getAsync('available_seats');
  return parseInt(seats);
};

const reserveSeatJob = (job, done) => {
  const seats = getCurrentAvailableSeats();
  if (seats <= 0) {
    done(new Error('Not enough seats available'));
  } else {
    reserveSeat(seats - 1);
    done();
  }
};

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
  } else {
    const job = queue.create('reserve_seat').save((err) => {
      if (err) {
        res.json({ status: 'Reservation failed' });
      } else {
        res.json({ status: 'Reservation in process' });
      }
    });
    job.on('complete', (result) => {
      console.log(`Seat reservation job ${job.id} completed`);
    });
    job.on('failed', (errorMessage) => {
      console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
  }
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });
  const seats = await getCurrentAvailableSeats();
  if (seats === 0) {
    reservationEnabled = false;
  } else if (seats > 0) {
    queue.process('reserve_seat', async (job, done) => {
      try {
        await reserveSeatJob(job, done);
      } catch (error) {
        done(error.message);
      }
    });
  }
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
