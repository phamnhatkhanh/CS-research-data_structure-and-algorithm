export const createTestReducer = (state = {}, action) => {
  switch (action.type) {
    case "TEST_REGISTER_REQUEST":
      return {
        ...state,
        loading: true,
      };
    case "TEST_REGISTER_SUCCESS":
      return {
        ...state,
        loading: false,
        success: true,
        question: action.question.question,
        test: action.question.test,
        hasquestion: true,
      };
    case "TEST_REGISTER_FAILED":
      return {
        ...state,
        loading: false,
        error: "TEST Already Registred",
      };
    default:
      return state;
  }
};

export const updateReducer = (state = {}, action) => {
  switch (action.type) {
    case "TEST_UPDATE_REQUEST":
      return {
        ...state,
        loading: true,
      };
    case "TEST_UPDATE_SUCCESS":
      return {
        ...state,
        loading: false,
        success: true,
      };
    case "TEST_UPDATE_FAILED":
      return {
        ...state,
        loading: false,
        error: "TEST Already Registred",
      };
    default:
      return state;
  }
};

export const getAllTESTReducer = (state = { TESTs: [] }, action) => {
  switch (action.type) {
    case "GET_ALLTESTS_REQUEST":
      return {
        ...state,
        loading: true,
      };
    case "GET_ALLTESTS_SUCCESS":
      return {
        ...state,
        loading: false,
        TESTs: action.payload,
      };
    case "GET_ALLTESTS_FAILED":
      return {
        ...state,
        loading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};

export const deleteTESTReducer = (state = {}, action) => {
  switch (action.type) {
    case "DELETE_TESTS_REQUEST":
      return {
        ...state,
        loading: true,
      };
    case "DELETE_TESTS_SUCCESS":
      return {
        ...state,
        loading: false,
        success: true,
      };
    case "DELETE_TESTS_FAILED":
      return {
        ...state,
        loading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};
