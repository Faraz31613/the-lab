import * as types from "./types"

import initialState from "./init"

const reducer = (state = initialState, action) => {
    switch (action.type) {
        case types.SIGN_IN: {
            return {
                ...state,
                isSignedIn: true,
            }
        }
        default: return state;
    }
}

export default reducer