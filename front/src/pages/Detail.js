import React, { useEffect, useState } from "react";
import { useLocation, useParams } from "react-router-dom";
import { Loading } from "components/Loading";
import Layout from "components/Layout";
import { hotelDetail } from "action/HotelSearch";
import MapContainer from "action/MapContainer";

const Detail = () => {
    const [loading, setLoading] = useState(false);
    const [detail, setDetail] = useState([]);
    const { _id } = useParams();
    console.log("params id ===> ", _id);

    // detail components 접속 시 스크롤 최상단으로 이동
    const { pathname } = useLocation();
    useEffect(() => {
        window.scrollTo(0, 0);
    }, [pathname]);

    useEffect(() => {
        async function getHotel() {
            setLoading((cur) => !cur);
            try {
                const response = await hotelDetail(_id);

                setDetail(response.data.data);
                setLoading((cur) => !cur);
            } catch (e) {
                console.log("axios get Error");
            }
        }
        getHotel();
    }, []);

    useEffect(() => {
        console.log("api ===> ", detail);
    }, [detail]);

    return (
        <Layout>
            <div className=" w-full min-h-screen mt-24 ">
                <h1 className="text-5xl text-center m-5 font-semibold text-yellow-500">
                    ⌨
                </h1>
                {/* <h1 className="text-4xl text-center">⌨</h1> */}

                {loading ? (
                    <Loading />
                ) : (
                    <div className="flex justify-center flex-col">
                        <div className="w-full items-center justify-center flex">
                            <div className="hero min-h-screen w-3/4 bg-base-200  ">
                                <div className="md:flex-col hero-content flex-row ">
                                    <img
                                        // src="https://api.lorem.space/image/movie?w=260&h=400"
                                        src={detail.hotel_img_url}
                                        alt="img"
                                        className="max-w-sm rounded-lg shadow-2xl"
                                    />
                                    <div>
                                        <h1 className="text-5xl font-bold">
                                            {detail.hotel_name}
                                        </h1>
                                        <span className="badge text-sm mt-2">
                                            {detail.region}
                                        </span>

                                        <div className="mt-5">
                                            <button
                                                className="btn btn-primary"
                                                onClick={() =>
                                                    window.open(
                                                        detail.hotel_url,
                                                        "_blank"
                                                    )
                                                }
                                            >
                                                Get Reservation
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="flex flex-col items-center justify-center">
                            지도
                            <MapContainer
                                searchPlace={detail.hotel_name}
                                region={detail.region}
                            />
                        </div>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default Detail;
