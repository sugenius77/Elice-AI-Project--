import React, { useEffect, useState } from "react";
import { toast } from "react-toastify";
import axios from "axios";

import EmptyHeartImg from "../components/img_src/heart1.png";
import HeartImg from "../components/img_src/heart2.png";

import { useRecoilValue } from "recoil";
import { userInfoState } from "../state/atom";
import { wishListState } from "../state/atom";

const HeartButton = ({ hotel_id, is_wish }) => {
    console.log("is_wish", is_wish);
    const [like, setLike] = useState(false);
    const userInfo = useRecoilValue(userInfoState);
    const wishList = useRecoilValue(wishListState);

    // console.log("userInfo ===> ", userInfo);
    // console.log("hotelid ===> ", hotel_id);
    console.log("is_wish ===> ", is_wish);

    // useEffect(() => {
    //     if (wishList.length > 2) {
    //         wishList.filter((hotel) => {
    //             if (hotel.hotel_id === hotel_id) {
    //                 setLike(true);
    //             }
    //         });
    //     }
    // }, []);

    React.useEffect(() => {
        if (is_wish) {
            setLike(true);
        }
    }, [is_wish]);

    const toggleLike = async (e) => {
        if (like === false) {
            try {
                let body = {
                    user_id: userInfo.id,
                    hotel_id: hotel_id,
                };
                const res = await axios.post(
                    `${process.env.REACT_APP_API}/wish-list/add`,
                    body
                );
                setLike((cur) => !cur);
                toast.success("Wish List에서 확인하세요.");
            } catch (err) {
                console.log(err);
                if (err.response.status == 400) {
                    toast.warning("Please Login");
                }
            }
        } else {
            const res = await axios
                .delete(
                    `${process.env.REACT_APP_API}/wish-list/${userInfo.id}/${hotel_id}`
                )
                .catch((e) => console.log(e));

            setLike((cur) => !cur);
        }
    };

    return (
        <div>
            <button
                onClick={toggleLike}
                className="btn btn-square btn-outline mr-2 bg-inherit hover:bg-white"
            >
                <img
                    className="w-5 h-5"
                    src={like ? HeartImg : EmptyHeartImg}
                    name="like"
                    alt="like-btn"
                />
            </button>
        </div>
    );
};
export default HeartButton;
