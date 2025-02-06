const scannerModel = require('../models/scannerModel');
const ScanResult = require('../models/scanResultModel');

async function scanWebsite(req, res, next) {
    const { url } = req.query;
    if (!url) {
        return res.status(400).json({ error: 'Please provide a URL to scan, e.g., /scan?url=https://example.com' });
    }

    try {
        const xssResults = await scannerModel.checkXSS(url);
        const sqlResults = await scannerModel.checkSQLInjection(url);

        // Save the results to MongoDB
        const newScanResult = new ScanResult({
            url,
            xssResults,
            sqlResults
        });

        await newScanResult.save();

        res.json({
            url,
            xssResults,
            sqlResults
        });
    } catch (error) {
        next(error); // Forward the error to the error handler
    }
}

function errorHandler(err, req, res, next) {
    console.error(err);
    res.status(500).json({ error: 'Internal Server Error' });
}

module.exports = { scanWebsite, errorHandler };
