import React from "react";

const Progressbar = ({ value }) => {
    let ref = React.useRef(0);
    const [effect, setEffect] = React.useState(false);

    React.useEffect(() => {
        const fn = () => {
            const myInter = setInterval(() => {
                // console.log("ref.current ", ref.current);
                setEffect((prev) => !prev);
                if (ref.current < value) ref.current++;
                else clearInterval(myInter);
            }, 10);
        };
        // console.log("ref", ref);
        if (ref.current !== undefined) fn();
    }, [ref]);

    return (
        //  {/* // Progress bar FIX 유사도 값 넣어야함 */}
        <div className="mt-2">
            <div className="w-full bg-gray-200 rounded-full">
                <div
                    className="bg-sub text-xs font-medium text-gray-500 text-center p-0.5 leading-none rounded-full"
                    style={{ width: `${ref.current}%` }}
                >
                    유사도 : {ref.current}%
                </div>
            </div>
        </div>
    );
};

export default Progressbar;
