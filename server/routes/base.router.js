const router = require("express").Router();
const multer  = require('multer')

const upload = multer({ dest: 'uploads/' })

router.post("/", upload.single("file"), (req, res) => {
  res.status(201);
});

module.exports = router;
