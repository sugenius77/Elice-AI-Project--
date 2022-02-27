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
            <div className=" w-full min-h-screen mt-24">
                <h1 className="text-4xl text-center m-5 font-semibold text-fontcolor">
                    호텔세심히
                </h1>
                <h1 className="text-4xl text-center">⌨</h1>
                {loading ? <Loading /> : <h1>{detail.title}</h1>}
            </div>
        </Layout>
    );
};

export default Detail;
