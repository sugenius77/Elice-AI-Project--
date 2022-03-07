import React, { useState } from "react";
import EmptyHeartImg from "./img_src/heart1.png";
import HeartImg from "./img_src/heart2.png";

import axios from "axios";

const HeartButton = ({ onClick, id }) => {
    const [like, setLike] = useState(false);

    const toggleLike = async (e) => {
        if (like === false) {
            // let body = {
            //     movie_id: resultmovieid,
            //     liked: 1,
            // };
            // const res = await axios
            //     .post("http://localhost:8000/result/mypage", body)
            //     .then((res) => setLikeNow(res.data.like_now))
            //     .catch((e) => console.log(e));

            setLike((cur) => !cur); // [POST] 사용자가 좋아요를 누름 -> DB 갱신
        } else {
            // let body = {
            //     movie_id: resultmovieid,
            //     liked: 0,
            // };
            // const res = await axios
            //     .post("http://localhost:8000/result/mypage", body)
            //     .then((res) => setLikeNow(res.data.like_now))
            //     .catch((e) => console.log(e));

            setLike((cur) => !cur);
        }
    };

    return (
        <div>
            <button
                onClick={toggleLike}
                className="btn btn-square btn-outline mr-2 bg-inherit"
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
