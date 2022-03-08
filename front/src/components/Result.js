import React, { useEffect, useRef, useState } from "react";
import { Loading, Loading2 } from "./Loading";
import { useRecoilState, useRecoilValue } from "recoil";
import {
    searchDataState,
    searchResultState,
    wishListIsDeletedState,
    userInfoState,
} from "../state/atom";
import { hotelSearch } from "../action/HotelSearch";
import HotelCard from "./cards/HotelCard";

const Result = () => {
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState([]);

    const searchData = useRecoilValue(searchDataState);
    const userInfo = useRecoilValue(userInfoState);
    const [isDeleted, setIsDeleted] = useRecoilState(wishListIsDeletedState);

    const [data, setData] = useState([]);

    const [target, setTarget] = useState(""); // target

    const [isLoading, setIsLoading] = useState(false);

    const loadData = async () => {
        setLoading(true);
        console.log(searchData);
        // 데이터가 온전히 들어오지 않았을 시
        // setGenres({ ...genres });
        try {
            const locals = searchData.region.join("|");
            console.log(locals);
            const response = await hotelSearch(searchData, locals, userInfo.id);
            // console.log(response.data.data);
            setResults(response.data.data);
            setData(response.data.data.slice(0, 5));

            setLoading(false);
        } catch (e) {
            console.log("axios get Error");
        }
    };
    useEffect(() => {
        loadData();
    }, [searchData]);

    useEffect(() => {
        console.log("Result API 가져온 data ===> ", results);
    }, [results]);

    useEffect(() => {
        if (isDeleted) {
            loadData();
            setIsDeleted(false);
        }
    }, [isDeleted]);
    let page = 0;

    const getMoreItem = async () => {
        setIsLoading(true);
        await new Promise((resolve) => setTimeout(resolve, 1100));
        page = page + 5;

        let movies;
        setResults((prev) => {
            movies = prev;
            return prev;
        });

        setData((cur) => {
            return [...cur].concat(movies.slice(page, page + 5));
        });

        setIsLoading(false);
    };

    const onIntersect = async ([entry], observer) => {
        if (entry.isIntersecting && !isLoading) {
            observer.unobserve(entry.target);
            await getMoreItem();
            observer.observe(entry.target);
        }
    };

    useEffect(() => {
        let observer;
        console.log("target", target);
        if (target) {
            observer = new IntersectionObserver(onIntersect, {
                threshold: 0.4,
            });
            observer.observe(target); // 타겟엘리먼트 지정
        }
        return () => observer && observer.disconnect();
    }, [target]);

    if (loading)
        return (
            <div className="mt-5">
                <Loading />
                <p className="text-2xl text-center font-reviewsFont my-10"></p>
            </div>
        );
    return (
        <>
            <div className=" gird justify-center md:mx-5 mx-32 mt-10 p-5 shadow-2xl bg-[#9DC3C2] items-center rounded-lg ">
                {data.map((h) => (
                    <HotelCard key={h.hotel_id} h={h} />
                ))}
            </div>
            {isLoading ? (
                <div>
                    <Loading2 />
                </div>
            ) : (
                ""
            )}
            <div
                // style={{ backgroundColor: "red", height: 1000 }}
                id="observer"
                ref={setTarget}
            ></div>
        </>
    );
};

export default Result;
