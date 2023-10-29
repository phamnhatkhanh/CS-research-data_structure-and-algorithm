import { applyMiddleware, combineReducers, createStore } from "redux";
import {
  addProductReducer,
  addProductReviewReducer,
  deleteProductReducer,
  getAllProductReducer,
  getProductByIdReducer,
  updateProductReducer,
} from "./reducers/product.reducer";
import thunk from "redux-thunk";
import { cartReducer } from "./reducers/cart.reducer";
import {
  deleteUserReducer,
  getAllUserReducer,
  loginReducer,
  registerUserReducer,
  updateReducer,
} from "./reducers/user.reducer";
import {
  getAllOrdersReducer,
  getOrderByIdReducer,
  getOrdersByUserIdReducer,
  placeOrderReducer,
} from "./reducers/order.reducer";
import { getAllAspectReviewsReducer } from "./reducers/review.reducer";

import { createTestReducer } from "./reducers/test.reducer";

const finalReducer = combineReducers({
  getAllProductsReducer: getAllProductReducer,
  getProductByIdReducer: getProductByIdReducer,
  cartReducer: cartReducer,
  registerNewUserReducer: registerUserReducer,
  loginReducer: loginReducer,
  placeOrderReducer: placeOrderReducer,
  getOrdersByUserIdReducer: getOrdersByUserIdReducer,
  getOrderByIdReducer: getOrderByIdReducer,
  getAllOrdersReducer: getAllOrdersReducer,
  addProductReviewReducer: addProductReviewReducer,
  updateReducer: updateReducer,
  getAllUsersReducer: getAllUserReducer,
  deleteUserReducer: deleteUserReducer,
  addProductReducer: addProductReducer,
  updateProductReducer: updateProductReducer,
  deleteProductReducer: deleteProductReducer,
  getAllAspectReviewsReducer: getAllAspectReviewsReducer,
  createTestReducer: createTestReducer,
});

const cartItems = localStorage.getItem("cartItems")
  ? JSON.parse(localStorage.getItem("cartItems"))
  : [];

const currentUser = localStorage.getItem("currentUser")
  ? JSON.parse(localStorage.getItem("currentUser"))
  : null;

const currentTest = localStorage.getItem("currentTest")
  ? JSON.parse(localStorage.getItem("currentTest"))
  : { loading: false, error: false, success: false };

const initialReducer = {
  cartReducer: { cartItems: cartItems },
  loginReducer: { currentUser: currentUser },
};

const store = createStore(finalReducer, initialReducer, applyMiddleware(thunk));

export default store;
