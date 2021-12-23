import React, { useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  TextInput,
  StyleSheet,
  SafeAreaView,
} from "react-native";
import { fetchApi } from "../../utils/fetch";

function Signup(props) {
  const userObj = {
    email,
    password,
    nickname,
    type,
  };

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [nickname, setNickname] = useState("");
  const [type, setType] = useState("");

  const handleEmail = (e) => {
    setEmail(e);
  };

  const handlePassword = (e) => {
    setPassword(e);
  };

  const handleNickname = (e) => {
    setNickname(e);
  };

  const handleType = (e) => {
    setType(e);
  };

  // const changeOutline = () => {
  //   setState({ outlineColor: "#A489E7" });
  // };

  const PostSignup = async () => {
    const [data] = await fetchApi({
      url: "http://localhost:8000/account/signup",
      method: "POST",
      data: {
        user: userObj,
      },
    });
    console.log(data);
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>회원가입</Text>
      </View>
      <View style={styles.layout}>
        <Text style={styles.content}>먼지의 여정, 함께라면 즐거워요!</Text>
        <View style={styles.inputContainer}>
          <Text style={styles.fieldLabel}>아이디</Text>
          <TextInput
            style={styles.input}
            placeholder="meonji@naver.com"
            placeholderTextColor="#707070"
            autoCapitalize="none"
            returnKeyType="next"
            onChangeText={(email) => handleEmail(email)}
            value={email}
            required
            // onFocus={() => changeOutline()}
          />
        </View>
        <View style={styles.inputContainer}>
          <Text style={styles.fieldLabel}>비밀번호</Text>
          <TextInput
            style={styles.input}
            placeholder="영문,숫자,특수문자"
            placeholderTextColor="#707070"
            autoCapitalize="none"
            returnKeyType="next"
            onChangeText={(password) => handlePassword(password)}
            value={password}
          />
        </View>
        <View style={styles.inputContainer}>
          <Text style={styles.fieldLabel}>닉네임</Text>
          <TextInput
            style={styles.input}
            placeholder="먼지 이름"
            placeholderTextColor="#707070"
            autoCapitalize="none"
            returnKeyType="next"
            onChangeText={(nickname) => handleNickname(nickname)}
            value={nickname}
          />
        </View>
        <View style={styles.inputContainer}>
          <Text style={styles.fieldLabel}>먼지타입</Text>
          <TextInput
            style={styles.input}
            placeholder="먼지 타입"
            placeholderTextColor="#707070"
            autoCapitalize="none"
            onChangeText={handleType}
            value={type}
          />
        </View>

        <TouchableOpacity
          style={styles.submitButton}
          onPress={() => PostSignup()}
        >
          <Text style={styles.submitButtonText}>별이 될래요</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

export default Signup;

const styles = StyleSheet.create({
  container: {
    paddingTop: 20,
    flex: 1,
    alignContent: "center",
  },
  header: {
    borderBottomColor: "#878787",
    borderBottomWidth: 1,
    padding: 15,
  },
  title: {
    fontSize: 20,
    fontWeight: "700",
    textAlign: "center",
  },
  content: {
    fontSize: 18,
    fontWeight: "500",
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
});
