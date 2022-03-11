import { atom } from "recoil";

export const LoginState = atom({
    key: "LoginState",
    default: { name: "Ryan", role: "Seller" },
    dangerouslyAllowMutability: true,
});

export const searchResultState = atom({
    key: "searchResultState",
    default: ["desktop", "notebook", "smart phone", "clock", "chair", "iPad"],
    dangerouslyAllowMutability: true,
});

export const userInfoState = atom({
    key: "userInfo",
    default: {},
    dangerouslyAllowMutability: true,
});

export const tokenState = atom({
    key: "tokenState",
    default: "",

    dangerouslyAllowMutability: true,
});

export const searchDataState = atom({
    key: "searchDataState",
    default: { region: ["000"], search: "바다뷰가 너무 좋았어요" },
    dangerouslyAllowMutability: true,
});

export const wishListState = atom({
    key: "wishListState",
    default: { data: [] },
    dangerouslyAllowMutability: true,
});

export const wishListIsDeletedState = atom({
    key: "wishListIsDeletedState",
    default: false,
    dangerouslyAllowMutability: true,
});
