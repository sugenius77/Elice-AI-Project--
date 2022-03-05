import axios from "axios";

export const hotelSearch = async (searchData, locals) =>
    await axios.get(
        `${process.env.REACT_APP_API}/hotel/recommend-hotel-list?region=${locals}&search=${searchData.search}`
    );

export const hotelDetail = async (_id) =>
    await axios.get(
        `${process.env.REACT_APP_API}/hotel/hotel-info?hotel_id=${_id}`
    );
