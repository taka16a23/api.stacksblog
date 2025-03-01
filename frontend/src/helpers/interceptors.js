import axios from "axios";

export default function axiosSetUp() {
  // API endpoint
  axios.defaults.baseURL = "<" + process.env.REACT_APP_API_URL + "/api/>";
  // enable send cookies
  axios.defaults.withCredentials = true
}
