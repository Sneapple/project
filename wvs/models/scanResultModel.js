const mongoose = require('mongoose');

const scanResultSchema = new mongoose.Schema({
    url: { type: String, required: true },
    xssResults: [String],
    sqlResults: [String],
    dateScanned: { type: Date, default: Date.now }
});

module.exports = mongoose.model('ScanResult', scanResultSchema);
