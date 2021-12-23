import "react-native-gesture-handler";
import React from "react";
import { NavigationContainer, StackActions } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";
import SignupPage from "./pages/SignupPage/Signup";
import ChallengePage from "./pages/ChallengePage/ChallengePage";
import DetailPage from "./pages/DetailPage";
import MakingPage from "./pages/MakingPage";
import TestPage from "./pages/TestPage";

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Signup">
        <Stack.Screen
          name="Challenge"
          component={ChallengePage}
          options={{ title: "챌린지 목록" }}
        />
        <Stack.Screen name="Signup" component={SignupPage} />
        <Stack.Screen
          name="Making"
          component={MakingPage}
          options={{
            title: "",
            headerStyle: {
              backgroundColor: "#674BAE",
            },
            headerTintColor: "white",
            headerTitleStyle: {
              fontWeight: "bold",
            },
          }}
        />
        <Stack.Screen name="Detail" component={DetailPage} />
      </Stack.Navigator>
    </NavigationContainer>
  );
  // return <SignupPage />;
  // return <ChallengePage />;
  // return <MakingPage />;
  // return <DetailPage />;
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F8F6FB",
    alignItems: "center",
    justifyContent: "center",
  },
});
