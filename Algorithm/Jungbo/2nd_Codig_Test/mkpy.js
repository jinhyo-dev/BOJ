const fs = require('fs').promises

for (let i = 65; i <= 69; i++) {
  var val = i
  var value = String.fromCharCode(val)
  fs.writeFile(`./D${value}.cpp`, '#include <iostream>\n using namespace std;\n int main()\n{\n}')
  .then(() => {
    return fs.readFile(`./D${value}.cpp`)
  })
  .then((data) => {
    console.log(data)
    console.log(data.toString())
  })
  .catch((err) => {
    console.log(err)
  })
}
