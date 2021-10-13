// let user = {
//   name : "Shikshya",
//   age : 22
// }



// const data = {
//   info :function () {
//     return this.name+ " your age is  " + this.age + " years old";
//   }
// }

// console.log(data.info.call(user))

// user6 = {
//   'a':2,
//   'b':3,
//   'c':4
// }

// console.log(user6)

let myObj = {
  name: 'sandy',
  age: 25,
  hobby : 'Coding'
};

const popitem = (obj) => {
  const keys = Object.keys(myObj);
  let lastObj = keys[keys.length - 1];
  delete obj[lastObj];
};

popitem(myObj);

console.log(myObj);

