import React from "react";
import {
  StyleSheet,
  Text,
  View,
  ScrollView,
  TouchableOpacity,
  Alert,
} from "react-native";

export default function DetailPage() {
  const popup = () => {
    Alert.alert("챌린지를 만들었습니다!");
  };
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>별별 챌린지 만들기</Text>
      <View style={styles.textContainer}>
        <Text style={styles.desc1}>챌린지명: </Text>
        <Text style={styles.desc2}>인원: </Text>
        <Text style={styles.desc2}>기간 : </Text>
        <Text style={styles.desc3}>설명: </Text>
        <TouchableOpacity style={styles.button} onPress={() => popup()}>
          <Text style={styles.buttonText}>만들기 완료</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#674BAE",
  },
  textContainer: {
    marginTop: "3%",
    backgroundColor: "white",
    borderWidth: 2,
    borderColor: "white",
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
    justifyContent: "center",
    alignItems: "center",
    height: 1000,
  },
  title: {
    marginTop: "10%",
    paddingLeft: "10%",
    paddingTop: "10%",
    fontSize: 20,
    fontWeight: "700",
    color: "#eee",
    paddingRight: 70,
  },
  desc1: {
    marginTop: "10%",
    color: "black",
  },
  desc2: {
    marginTop: "3%",
    color: "black",
  },
  desc3: {
    marginTop: "10%",
    marginBottom: "10%",
    color: "darkgrey",
  },
  button: {
    width: 100,
    marginBottom: "10%",
    padding: 10,
    borderWidth: 1,
    backgroundColor: "#A489E7",
    borderRadius: 7,
  },
  buttonText: {
    color: "#fff",
    textAlign: "center",
    borderColor: "rgba(41, 25, 101, 0.8)",
  },
});
