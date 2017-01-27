import { injectReducer } from "store/reducers"

export default (store) => ({
  path: "login",
  getComponent(nextState, cb) {
    require.ensure([], (require) => {
      const Login = require("./Login").default
      
      cb(null, Login);
    })
  }
})
