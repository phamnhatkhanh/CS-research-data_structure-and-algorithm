import axios from "axios";

export const createNewTest = (test) => (dispatch) => {
  dispatch({ type: "TEST_REGISTER_REQUEST" });

  axios
    .post("/tests", test)
    .then((res) => {
      dispatch({ type: "TEST_REGISTER_SUCCESS", question: res.data });
      // console.log(res.data);
    })
    .catch((err) => {
      dispatch({ type: "TEST_REGISTER_FAILED", payload: err });
      console.log(err);
    });
};

export const updateTest = (testid, updateTest) => (dispatch) => {
  dispatch({
    type: "TEST_UPDATE_REQUEST",
  });

  console.log(updateTest);

  axios
    .put(`/test/${testid}`, updateTest)
    .then((res) => {
      dispatch({
        type: "TEST_UPDATE_SUCCESS",
      });
      console.log(res);
      window.location.reload();
    })
    .catch((err) => {
      dispatch({
        type: "TEST_UPDATE_FAILED",
        payload: err,
      });
      console.log(err);
    });
};

export const getAllTests = () => (dispatch) => {
  dispatch({ type: "GET_ALLTESTS_REQUEST" });

  axios
    .get("/test")
    .then((res) => {
      dispatch({ type: "GET_ALLTESTS_SUCCESS", payload: res.data });
    })
    .catch((err) => {
      dispatch({ type: "GET_ALLTESTS_FAILED", payload: err });
    });
};

export const deleteTest = (testid) => (dispatch) => {
  dispatch({
    type: "DELETE_TEST_REQUEST",
  });

  axios
    .delete(`/test/${testid}`)
    .then((res) => {
      dispatch({
        type: "DELETE_TEST_SUCCESS",
        payload: res.data,
      });
      alert("Test deleted successfully");
      window.location.reload();
    })
    .catch((err) => {
      dispatch({
        type: "DELETE_TEST_FAILED",
        payload: err,
      });
    });
};
