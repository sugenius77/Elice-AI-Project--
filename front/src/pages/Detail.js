import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Loading } from "components/Loading";
import Layout from "components/Layout";
import { hotelDetail } from "action/HotelSearch";

const Detail = () => {
    const [loading, setLoading] = useState(false);
    const [detail, setDetail] = useState([]);
    const { _id } = useParams();
    console.log("params id ===> ", _id);

    useEffect(() => {
        async function getHotel() {
            setLoading((cur) => !cur);
            try {
                const response = await hotelDetail(_id);

                setDetail(response.data.data.movie);
                setLoading((cur) => !cur);
            } catch (e) {
                console.log("axios get Error");
            }
        }
        getHotel();
    }, []);

    console.log(detail);

    return (
        <Layout>
            <div className=" w-full min-h-screen mt-24 ">
                <h1 className="text-4xl text-center m-5 font-semibold text-fontcolor">
                    호텔세심히
                </h1>
                <h1 className="text-4xl text-center">⌨</h1>

                {loading ? (
                    <Loading />
                ) : (
                    <div className="flex justify-center">
                        <div className="hero min-h-screen bg-base-200 w-3/4 ">
                            <div className="md:flex-col hero-content flex-row">
                                <img
                                    src="https://api.lorem.space/image/movie?w=260&h=400"
                                    alt="img"
                                    className="max-w-sm rounded-lg shadow-2xl"
                                />
                                <div>
                                    <h1 className="text-5xl font-bold">
                                        {detail.title}
                                    </h1>
                                    <p className="py-6">
                                        Lorem ipsum dolor sit amet consectetur
                                        adipisicing elit. Libero magnam
                                        laboriosam voluptate quod aut eos. Sequi
                                        molestiae sint sunt unde.
                                    </p>
                                    <button className="btn btn-primary">
                                        Get Reservation
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default Detail;
