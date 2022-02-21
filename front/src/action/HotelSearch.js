import axios from "axios";

export const hotelSearch = async (searchData) =>
    await axios.post(`${process.env.REACT_APP_API}/hotels`, searchData);
