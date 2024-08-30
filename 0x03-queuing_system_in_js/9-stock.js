const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const client = redis.createClient();

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Function to get item by id
function getItemById(id) {
  return listProducts.find(item => item.id === id);
}

// Route to get list of products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(item => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  })));
});

// Function to reserve stock by item id
function reserveStockById(itemId, stock) {
  const setAsync = promisify(client.set).bind(client);
  return setAsync(`item.${itemId}`, stock);
}

// Async function to get current reserved stock by item id
async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
}

// Route to get product details by item id
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (item) {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
      currentQuantity
    });
  } else {
    res.json({ status: 'Product not found' });
  }
});

// Route to reserve a product by item id
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (item) {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    if (currentQuantity >= 1) {
      res.json({ status: 'Not enough stock available', itemId });
    } else {
      await reserveStockById(itemId, 1);
      res.json({ status: 'Reservation confirmed', itemId });
    }
  } else {
    res.json({ status: 'Product not found' });
  }
});

// Start the server
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
