import React from "react";
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableOpacity,
  ScrollView,
  Platform,
} from "react-native";

const main =
  "https://firebasestorage.googleapis.com/v0/b/sparta-image.appspot.com/o/lecture%2Fmain.png?alt=media&token=8e5eb78d-19ee-4359-9209-347d125b322c";
import data from "../../data.json";
import Card from "../../components/Card";

export default function ChallengePage() {
  let tip = data.tip;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Challenge List</Text>
      <View style={styles.middleContainer}></View>
      <ScrollView>
        <View style={styles.cardContainer}>
          {/* 하나의 카드 영역을 나타내는 View */}
          {tip.map((content, i) => {
            return <Card content={content} key={i} />;
          })}
        </View>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    //앱의 배경 색
    backgroundColor: "#F8F6FB",
  },
  title: {
    //폰트 사이즈
    fontSize: 20,
    //폰트 두께
    fontWeight: "700",
    //위 공간으로 부터 이격
    marginTop: 50,
    //왼쪽 공간으로 부터 이격
    marginLeft: 20,
  },

  mainImage: {
    //컨텐츠의 넓이 값
    width: "90%",
    //컨텐츠의 높이 값
    height: 200,
    //컨텐츠의 모서리 구부리기
    borderRadius: 10,
    marginTop: 20,
    //컨텐츠 자체가 앱에서 어떤 곳에 위치시킬지 결정(정렬기능)
    //각 속성의 값들은 공식문서에 고대로~ 나와 있음
    alignSelf: "center",
  },
  middleContainer: {
    marginTop: 20,
    marginLeft: 10,
    height: 60,
  },
  middleButton01: {
    width: 100,
    height: 50,
    padding: 15,
    backgroundColor: "#fdc453",
    borderColor: "deeppink",
    borderRadius: 15,
    margin: 7,
  },
  middleButtonText: {
    color: "#fff",
    fontWeight: "700",
    //텍스트의 현재 위치에서의 정렬
    textAlign: "center",
  },
  cardContainer: {
    marginTop: 10,
    marginLeft: 10,
  },
});
