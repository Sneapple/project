const express = require('express');
const mongoose = require('mongoose');
const path = require('path');
const scannerRoutes = require('./routes/scannerRoutes');

const app = express();
const PORT = 5091;

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/vulnerability-scanner', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch((error) => console.error('MongoDB connection error:', error));

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'views')));

// Routes
app.use('/', scannerRoutes);

let server = null;

// Start the server
if (process.env.NODE_ENV !== 'test') {
    server = app.listen(PORT, () => {
        console.log(`Server is running on http://127.0.0.1:${PORT}`);
    });
}

// Export the app and server instance
module.exports = { app, server };
