import React, { useEffect, useState } from "react";
import { useHistory, useLocation, useParams } from "react-router-dom";
import { Loading } from "../components/Loading";
import Layout from "../components/Layout";

import { hotelDetail } from "../action/HotelSearch"; // api 호출을 위한 import

import MapContainer from "../action/MapContainer";
import DetailReview from "../action/DetailReview";
import DetailKeywords from "../action/DetailKeywords";
import HeartButton from "../action/HeartButton";

const Detail = ({ location }) => {
    const [loading, setLoading] = useState(true);
    const [detail, setDetail] = useState([]);
    const { _id } = useParams();
    const history = useHistory();

    const hotel_id = location.state.hotel_id;
    const is_wish = location.state.is_wish;

    console.log("params id ===> ", _id);
    console.log("is_wish ===> ", is_wish);

    // detail components 접속 시 스크롤 최상단으로 이동
    const { pathname } = useLocation();
    useEffect(() => {
        window.scrollTo(0, 0);
    }, [pathname]);

    useEffect(() => {
        async function getHotel() {
            try {
                const response = await hotelDetail(_id);

                setDetail(response.data.data);
                setLoading(false);
            } catch (e) {
                console.log("axios get Error");
            }
        }
        getHotel();
    }, []);

    useEffect(() => {
        console.log("detail state  ===> ", detail);
    }, [loading]);

    return (
        <Layout>
            <div className=" w-full min-h-screen mt-24 ">
                {loading ? (
                    <Loading />
                ) : (
                    <div className="flex flex-col">
                        <div className="w-full items-center justify-center flex mb-5 p-3">
                            <div className="block hero w-3/4 bg-base-200 md:w-full  ">
                                <div className="md:flex-col justify-start hero-content flex-row cursor-default ">
                                    <img
                                        // src="https://api.lorem.space/image/movie?w=260&h=400"
                                        src={detail.hotel_img_url}
                                        alt="img"
                                        className="max-w-sm rounded-lg shadow-2xl"
                                    />
                                    <div>
                                        <h1 className="text-5xl font-bold text-shadow-sm font-notoSans md:text-3xl ">
                                            {detail.hotel_name}
                                        </h1>
                                        <span className="badge text-lg bg-[#004E98] border-0 outline-none mt-2">
                                            {detail.region}
                                        </span>
                                        <span className="text-sm ml-1">
                                            {detail.address}
                                        </span>

                                        <div className="mt-5">
                                            <div className="flex">
                                                <button
                                                    className="btn btn-primary bg-[#F6bD60] hover:bg-[#FFC145] outline-none border-0"
                                                    onClick={() =>
                                                        window.open(
                                                            detail.hotel_url,
                                                            "_blank"
                                                        )
                                                    }
                                                >
                                                    예약 바로가기
                                                </button>
                                                <span className="ml-1">
                                                    <HeartButton
                                                        hotel_id={hotel_id}
                                                        is_wish={is_wish}
                                                    />
                                                </span>
                                            </div>
                                            <div className="font-notoSans my-5">
                                                <DetailKeywords
                                                    data={
                                                        detail.positive_keywords
                                                    }
                                                    positive={true}
                                                />
                                                <DetailKeywords
                                                    data={
                                                        detail.negative_keywords
                                                    }
                                                />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <hr />
                            </div>
                        </div>
                        <div className="flex justify-center">
                            <div className="  w-3/4 bg-base-200  ">
                                <div className="flex md:flex-col w-full flex-row cursor-default">
                                    <div className="flex flex-col w-1/2  md:w-full">
                                        <p className="font-semibold w-full border-2 rounded-full text-center my-2 font-notoSans border-blue-200 text-xl">
                                            😃긍정 경험
                                        </p>
                                        <div className="example grid flex-grow overflow-auto h-80 card bg-[#F5F1ED] rounded-box place-items-center w-full">
                                            <DetailReview
                                                reviews={detail.reviews}
                                                positive={1}
                                            />
                                        </div>
                                    </div>
                                    <div className="md:divider divider-horizontal"></div>
                                    <div className="flex flex-col w-1/2 md:w-full">
                                        <p className="font-semibold w-full border-2 rounded-full text-center my-2 font-notoSans border-red-200 text-xl">
                                            😰부정 경험
                                        </p>
                                        <div className="example grid flex-grow overflow-y-auto h-80 card bg-[#F5F1ED] rounded-box place-items-center w-full ">
                                            <DetailReview
                                                reviews={detail.reviews}
                                                positive={0}
                                            />
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="flex flex-col items-center justify-center  my-4">
                            <div class="flex justify-center gap-1 my-1 w-full cursor-default">
                                <kbd className="kbd">m</kbd>
                                <kbd className="kbd">a</kbd>
                                <kbd className="kbd">p</kbd>
                            </div>
                            <MapContainer
                                searchPlace={detail.hotel_name}
                                region={detail.region}
                                address={detail.address}
                            />
                        </div>
                        <div className="flex items-center justify-center m-5">
                            <button
                                className="btn"
                                onClick={() => {
                                    history.goBack();
                                }}
                            >
                                검색으로 돌아가기
                            </button>
                        </div>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default Detail;
