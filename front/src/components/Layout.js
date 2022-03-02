import React from "react";
import Footer from "components/Footer";

const Layout = ({ children, id }) => {
    return (
        <div id={id}>
            <div className="content overflow-x-hidden font-doogle bg-primary">
                {children}
            </div>
            <Footer />
        </div>
    );
};

export default Layout;
