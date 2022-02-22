import axios from "axios";

export const hotelSearch = async (searchData) =>
    await axios.post(`${process.env.REACT_APP_API}/hotels`, searchData);

export const hotelDetail = async (_id) =>
    await axios.get(`https://yts.mx/api/v2/movie_details.json?movie_id=${_id}`);
