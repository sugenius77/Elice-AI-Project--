import React, { useEffect, useState } from "react";
import { useHistory, useLocation, useParams } from "react-router-dom";
import { Loading } from "components/Loading";
import Layout from "components/Layout";

import { hotelDetail } from "action/HotelSearch";

import MapContainer from "action/MapContainer";
import DetailReview from "action/DetailReview";

const Detail = () => {
    const [loading, setLoading] = useState(true);
    const [detail, setDetail] = useState([]);
    const { _id } = useParams();
    const history = useHistory();
    console.log("params id ===> ", _id);

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
    }, [detail]);

    return (
        <Layout>
            <div className=" w-full min-h-screen mt-24 ">
                {loading ? (
                    <Loading />
                ) : (
                    <div className="flex flex-col">
                        <div className="w-full items-center justify-center flex">
                            <div className="block hero w-3/4 bg-base-200  ">
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
                                        <span className="badge text-xl mt-2">
                                            {detail.region}
                                        </span>

                                        <div className="mt-5">
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
                                            <div className="font-notoSans mb-2">
                                                <p className="my-2">
                                                    ▶︎리뷰로 보는 핵심 키워드
                                                </p>
                                                <kbd className="kbd text-sm font-notoSans border-blue-200">
                                                    고급스러움
                                                </kbd>
                                                <kbd className="kbd text-sm font-notoSans border-blue-200">
                                                    접근성
                                                </kbd>
                                                <kbd className="kbd text-sm font-notoSans border-blue-200">
                                                    친절
                                                </kbd>
                                            </div>
                                            <div className="font-notoSans">
                                                <kbd className="kbd text-sm font-notoSans border-red-200">
                                                    유료
                                                </kbd>
                                                <kbd className="kbd text-sm font-notoSans border-red-200">
                                                    더러운
                                                </kbd>
                                                <kbd className="kbd text-sm font-notoSans border-red-200">
                                                    가성비가 별로
                                                </kbd>
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
