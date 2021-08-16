import * as types from "./types"


export const signIn = (username, password) => {
    return {
        type: types.SIGN_IN,
        payload: {username, password}
    }
}

