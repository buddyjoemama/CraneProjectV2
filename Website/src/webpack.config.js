var path = require('path');

module.exports = {
  //...
  devServer: {
    contentBase: path.join(__dirname, 'src'),
    compress: true,
    port: 9000,
    index: 'src/Index.html',
    watchContentBase: true
  }
};