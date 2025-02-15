const express = require('express');
const path = require('path');
const scannerController = require('../controllers/scannerController');

const router = express.Router();

// Route to serve the home page
router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../views/index.html'));
});

// Route to serve the result page
router.get('/result', (req, res) => {
  res.sendFile(path.join(__dirname, '../views/result.html'));
});

// Route to scan a website
router.get('/scan', scannerController.scanWebsite); 

// Error handler middleware
router.use(scannerController.errorHandler);

module.exports = router;
