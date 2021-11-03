module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: ["standard"],
  parserOptions: {
    ecmaVersion: 13,
  },
  rules: {
    "max-len": [2, 80, 4],
  },
};
