import React, { useRef, useState } from "react";
import { userState, tokenState } from "state/atom";
import { useRecoilState } from "recoil";
import { useEffect } from "react";

import { Loading, Loading2 } from "components/Loading";
import axios from "axios";

const TestResult = () => {
    const [itemList, setItemList] = useState([
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22,
    ]); // ItemList

    const [movies, setMovies] = useState([]);
    const [data, setData] = useState([]);

    const [target, setTarget] = useState(""); // target

    const [isLoading, setIsLoading] = useState(false);
    const [apiLoading, setApiIsLoading] = useState(false);

    useEffect(() => {
        async function loadData() {
            setApiIsLoading(true);
            try {
                const response = await axios.get(
                    `https://yts.mx/api/v2/list_movies.json?minimum_rating=8&sort_by=year`
                );
                setMovies(response.data.data.movies);
                setData(response.data.data.movies.slice(0, 5));

                console.log("get api");
                setApiIsLoading(false);
            } catch (e) {
                console.log("axios get Error");
            }
        }
        loadData();
    }, []);

    // const fetchItems = async () => setItemIndex((prev) => prev + 5);

    useEffect(() => {
        console.log(itemList);
    }, [itemList]);

    let page = 0;

    const getMoreItem = async () => {
        setIsLoading(true);
        await new Promise((resolve) => setTimeout(resolve, 2000));
        page = page + 5;
        setData((cur) => [...cur].concat(movies.slice(page, page + 5)));

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
        console.log("data state ===>", data);
        console.log("movies ===>", movies);
    }, [data]);

    useEffect(() => {
        let observer;
        if (target) {
            observer = new IntersectionObserver(onIntersect, {
                threshold: 0.4,
            });
            observer.observe(target); // 타겟엘리먼트 지정
        }
        return () => observer && observer.disconnect();
    }, [target]);

    return (
        <div className="app">
            {apiLoading ? (
                <div className="min-h-screen">
                    <Loading2></Loading2>
                </div>
            ) : (
                <div className="w-full h-full flex flex-col justify-center text-center items-center">
                    {data.map((item, index) => (
                        <div
                            className="w-80 h-24 flex flex-col bg-red-100 m-2 shadow-sm rounded-r"
                            key={index}
                        >
                            {item.title}
                        </div>
                    ))}
                </div>
            )}

            {isLoading ? (
                <div>
                    <Loading></Loading>
                </div>
            ) : (
                ""
            )}
            <div ref={setTarget}></div>
        </div>
    );
};

export default TestResult;
