var path = require('path');

module.exports = {
  //...
  devServer: {
    contentBase: path.join(__dirname, 'StaticSite'),
    compress: true,
    port: 9000,
    index: 'StaticSite/Index.html',
    watchContentBase: true
  }
};