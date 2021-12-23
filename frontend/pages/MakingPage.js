import React from "react";
import {
  StyleSheet,
  Text,
  View,
  ScrollView,
  TouchableOpacity,
  Alert,
} from "react-native";

export default function MakingPage({ navigation }) {
  const popup = () => {
    Alert.alert("챌린지를 만들었습니다!");
  };
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>별별 챌린지 만들기</Text>
      {/* <View style={styles.textContainer}>
        <Text style={styles.desc1}>챌린지명: </Text>
        <Text style={styles.desc2}>인원: </Text>
        <Text style={styles.desc2}>기간 : </Text>
        <Text style={styles.desc3}>설명: </Text>
        <TouchableOpacity style={styles.button} onPress={() => popup()}>
          <Text style={styles.buttonText}>만들기 완료</Text>
        </TouchableOpacity>
      </View> */}
      <View style={styles.layout}>
        <Text style={styles.content}>먼지의 여정, 함께라면 즐거워요!</Text>
        <View style={styles.inputContainer}>
          <Text style={styles.fieldLabel}>챌린지명</Text>
          <TextInput
            style={styles.input}
            placeholder="달성하고 싶은 목표를 담은 이름!"
            placeholderTextColor="#707070"
            autoCapitalize="none"
            returnKeyType="next"
            onChangeText={(title) => handleTitle(title)}
            value={title}
            required
            // onFocus={() => changeOutline()}
          />
        </View>
        <View style={styles.inputContainer}>
          <Text style={styles.fieldLabel}>최대인원</Text>
          <TextInput
            style={styles.input}
            placeholder="5"
            placeholderTextColor="#707070"
            autoCapitalize="none"
            returnKeyType="next"
            onChangeText={(max_people) => handleMax(max_people)}
            value={max_people}
          />
        </View>
        <View style={styles.inputContainer}>
          <Text style={styles.fieldLabel}>챌린지 기간</Text>
          <TextInput
            style={styles.input}
            placeholder=""
            placeholderTextColor="#707070"
            autoCapitalize="none"
            returnKeyType="next"
            onChangeText={(period) => handlePeriod(period)}
            value={period}
          />
        </View>
        <View style={styles.inputContainer}>
          <Text style={styles.fieldLabel}>설명</Text>
          <TextInput
            style={styles.input}
            placeholder="먼지 타입"
            placeholderTextColor="#707070"
            autoCapitalize="none"
            value={description}
          />
        </View>

        <TouchableOpacity
          style={styles.submitButton}
          // onPress={() => PostSignup()}
          onPress={() => navigation.navigate("Detail")}
        >
          <Text style={styles.submitButtonText}>별이 될래요</Text>
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
    fontWeight: "800",
    color: "#eee",
    paddingRight: 70,
  },
  layout: {
    flex: 1,
    height: "auto",
    paddingTop: "10%",
    paddingBottom: "10%",
    flexDirection: "column",
    justifyContent: "center",
    alignContent: "center",
    alignItems: "center",
  },
  inputContainer: {
    width: "85%",
    flexDirection: "row",
    justifyContent: "space-between",
    alignContent: "space-around",
    marginTop: "5%",
  },
  fieldLabel: {
    fontSize: 18,
    fontWeight: "500",
    marginTop: 50,
    marginLeft: 20,
  },
  input: {
    margin: 30,
    width: "55%",
    height: "80%",
    backgroundColor: "#E5E5E5",
    borderColor: "transparent",
    borderRadius: 10,
    borderWidth: 1,
  },
  submitButton: {
    backgroundColor: "#A489E7",
    borderRadius: 80,
    padding: 10,
    margin: 50,
    width: "80%",
    height: "10%",
    justifyContent: "center",
  },
  submitButtonText: {
    fontSize: 20,
    color: "white",
    textAlign: "center",
  },
  // desc1: {
  //   marginTop: "10%",
  //   color: "black",
  // },
  // desc2: {
  //   marginTop: "3%",
  //   color: "black",
  // },
  // desc3: {
  //   marginTop: "10%",
  //   marginBottom: "10%",
  //   color: "darkgrey",
  // },
  // button: {
  //   width: 100,
  //   marginBottom: "10%",
  //   padding: 10,
  //   borderWidth: 1,
  //   backgroundColor: "#A489E7",
  //   borderRadius: 7,
  // },
  // buttonText: {
  //   color: "#fff",
  //   textAlign: "center",
  //   borderColor: "rgba(41, 25, 101, 0.8)",
  // },
});
