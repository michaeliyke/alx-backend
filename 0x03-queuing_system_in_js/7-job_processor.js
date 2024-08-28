const queue = require('kue').createQueue();

const blacklistedNumbers = [4153518780, 4153518781];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100, { percentage: '0%' });
  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    return done(error);
  }

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  job.progress(50, 100, { percentage: '50%' });
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
