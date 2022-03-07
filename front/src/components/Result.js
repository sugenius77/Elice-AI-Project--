import React, { useEffect, useRef, useState } from "react";
import { Loading, Loading2 } from "./Loading";

import { useRecoilState, useRecoilValue } from "recoil";
import { searchDataState, searchResultState, testState } from "../state/atom";

import { hotelSearch } from "../action/HotelSearch";
import HotelCard from "./cards/HotelCard";

const Result = () => {
    const [loading, setLoading] = useState(false);
    const [searchData, setSearchData] = useRecoilState(searchDataState);
    const [results, setResults] = useState([]);
    const testdata = useRecoilValue(testState);

    const [data, setData] = useState([]);

    const [target, setTarget] = useState(""); // target

    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        async function loadData() {
            setLoading(true);
            console.log(searchData);
            // 데이터가 온전히 들어오지 않았을 시
            // setGenres({ ...genres });
            try {
                const locals = searchData.region.join("|");
                console.log(locals);
                const response = await hotelSearch(searchData, locals);
                // console.log(response.data.data);
                setResults(response.data.data);
                setData(response.data.data.slice(0, 5));

                console.log("API 가져온 data ===> ", results);
                setLoading(false);
            } catch (e) {
                console.log("axios get Error");
            }
        }
        loadData();
    }, [searchData]);

    let page = 0;

    const getMoreItem = async () => {
        setIsLoading(true);
        await new Promise((resolve) => setTimeout(resolve, 2000));
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
                <p className="text-2xl text-center font-reviewsFont">
                    Loading...
                </p>
            </div>
        );
    return (
        <div>
            <div className=" gird justify-center md:mx-5 mx-32 mt-10 shadow-2xl bg-sub items-center rounded-lg">
                {data.map((h) => (
                    <HotelCard key={h.hotel_id} h={h} />
                ))}
            </div>
            {isLoading ? (
                <div>
                    <Loading2></Loading2>
                </div>
            ) : (
                ""
            )}
            <div
                // style={{ backgroundColor: "red", height: 1000 }}
                id="observer"
                ref={setTarget}
            ></div>
        </div>
    );
};

export default Result;
