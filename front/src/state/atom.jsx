import { atom, selector } from "recoil";

export const LoginState = atom({
  key: "LoginState",
  default: { name: "Ryan", role: "Seller" },
  dangerouslyAllowMutability: true,
});

export const testState = atom({
  key: "testState",
  default: [
    {
      _id: "1",
      title: "라마다호텔",
      review: "여긴 바다뷰가 정말 최고네요",
      content: "좋은곳",
      location: "서울 근처",
      price: 200,
    },
    {
      _id: "2",
      title: "샘모텔",
      review: "창문이 없어서 오래오래 깊은 잠을 잘 수 있어요",
      content: "안좋은곳",
      location: "서울 근처",
      price: 100,
    },
    {
      _id: "3",
      title: "포포인츠쉐르빌",
      review: "쉐라톤인줄 알고 왔는데 생각보다 호캉스할만해요. 바다뷰도 좋아요",
      content: "괜찮은곳",
      location: "서울 근처",
      price: 300,
    },
    {
      _id: 1,
      title: "라마다호텔",
      review: "여긴 바다뷰가 정말 최고네요",
      content: "좋은곳",
      location: "서울 근처",
      price: 200,
    },
    {
      _id: 2,
      title: "샘모텔",
      review: "창문이 없어서 오래오래 깊은 잠을 잘 수 있어요",
      content: "안좋은곳",
      location: "서울 근처",
      price: 100,
    },
    {
      _id: 3,
      title: "포포인츠쉐르빌",
      review: "쉐라톤인줄 알고 왔는데 생각보다 호캉스할만해요. 바다뷰도 좋아요",
      content: "괜찮은곳",
      location: "서울 근처",
      price: 300,
    },
  ],
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
  default: {},
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
