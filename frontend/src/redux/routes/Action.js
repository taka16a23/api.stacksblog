import {
  ROUTES,
} from "../constants/";

export const setRoutes = (payload) => {
    return {
        type: ROUTES,
        payload
    }
}
