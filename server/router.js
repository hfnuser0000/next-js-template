const express = require("express");
const router = express.Router();

router.get("/rss/default/:rssname", async (req, res) => {
    return res.send('OK');
});

module.exports = router;
