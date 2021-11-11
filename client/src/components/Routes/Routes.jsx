import React from "react";
import { Redirect, Route, Switch } from "react-router-dom";
import Dashboard from "../Plots/dashboard.js";

export default function Routes() {
	return (
		<Switch>
			<Route exact path="/">
				<Dashboard />
			</Route>
		</Switch>
	);
}
