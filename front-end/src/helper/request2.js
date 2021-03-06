import axios from "axios";

const instance = axios.create({ baseURL: "http://localhost:8000/api" });

instance.interceptors.response.use(
  response => {
    const { status, data } = response;
    if (status === 200) {
      return Promise.resolve(data);
    }
    return Promise.reject(response.data);
  },
  error => Promise.reject(error)
);

export default instance;
