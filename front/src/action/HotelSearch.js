import axios from "axios";

export const hotelSearch = async (searchData, locals, id) =>
    await axios.get(
        `${process.env.REACT_APP_API}/hotel/recommend-hotel-list?region=${locals}&search=${searchData.search}&user_id=${id}`
    );

export const hotelDetail = async (_id) =>
    await axios.get(
        `${process.env.REACT_APP_API}/hotel/hotel-info?hotel_id=${_id}`
    );

export function randomValueFromArray() {
    let last_name = [
        "김",
        "이",
        "박",
        "최",
        "정",
        "강",
        "조",
        "윤",
        "장",
        "임",
        "한",
        "오",
        "서",
        "남궁",
        "탁",
        "차",
        "황",
    ];
    const random = Math.floor(Math.random() * last_name.length);
    return last_name[random];
}
