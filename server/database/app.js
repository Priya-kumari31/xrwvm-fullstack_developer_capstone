const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');

const app = express();
const port = 3030;

app.use(cors());
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// Load JSON data
const reviews_data = JSON.parse(fs.readFileSync("data/reviews.json", 'utf8'));
const dealerships_data = JSON.parse(fs.readFileSync("data/dealerships.json", 'utf8'));
// MongoDB connection
mongoose.connect("mongodb://mongo_db:27017/", {
  dbName: 'dealershipsDB'
});

// Models
const Reviews = require('./review');
const Dealerships = require('./dealership');

// Seed database (FIXED - no await outside function)
(async function seedDB() {
  try {
    await Reviews.deleteMany({});
    await Reviews.insertMany(reviews_data.reviews);

    await Dealerships.deleteMany({});
    await Dealerships.insertMany(dealerships_data.dealerships);

    console.log("Database seeded successfully");
  } catch (err) {
    console.log(err);
  }
})();

// Home route
app.get('/', (req, res) => {
  res.send("Welcome to the Mongoose API");
});

// Fetch all reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    const docs = await Reviews.find();
    res.json(docs);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Fetch reviews by dealer
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const docs = await Reviews.find({ dealership: req.params.id });
    res.json(docs);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ✅ FIXED: fetch all dealers
app.get('/fetchDealers', async (req, res) => {
  try {
    const docs = await Dealerships.find();
    res.json(docs);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ✅ FIXED: fetch dealers by state
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const docs = await Dealerships.find({ state: req.params.state });
    res.json(docs);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ✅ FIXED: fetch dealer by id
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    const docs = await Dealerships.findOne({ id: parseInt(req.params.id) });
    res.json(docs);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Insert review
app.post('/insert_review', express.raw({ type: '*/*' }), async (req, res) => {
  try {
    const data = JSON.parse(req.body);

    const last = await Reviews.find().sort({ id: -1 });
    let new_id = last.length ? last[0].id + 1 : 1;

    const review = new Reviews({
      id: new_id,
      name: data.name,
      dealership: data.dealership,
      review: data.review,
      purchase: data.purchase,
      purchase_date: data.purchase_date,
      car_make: data.car_make,
      car_model: data.car_model,
      car_year: data.car_year
    });

    const saved = await review.save();
    res.json(saved);

  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});