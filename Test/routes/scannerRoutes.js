const express = require('express');
const scannerController = require('../controllers/scannerController'); // Only this line
const router = express.Router();

router.post('/scan', scannerController.scan);

module.exports = router;

