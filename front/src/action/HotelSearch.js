import axios from "axios";

export const hotelSearch = async (searchData, locals) =>
    await axios.get(
        `${process.env.REACT_APP_API}/hotel/recommendHotelList?region=${locals}&search=${searchData.search}`
    );

export const hotelDetail = async (_id) =>
    await axios.get(`https://yts.mx/api/v2/movie_details.json?movie_id=${_id}`);
