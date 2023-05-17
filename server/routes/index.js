const router = require("express").Router();

const baseRouter = require("./base.router");

function routerApi(app) {
  // Over writing default base path
  app.use("/api/v1", router);

  // Base path routes
  router.use("/", baseRouter);
}

module.exports = routerApi;
