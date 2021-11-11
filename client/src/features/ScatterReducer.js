import { createSlice } from '@reduxjs/toolkit';

const initialStates = {league: "england", per90s: 5,
title: "Title", xlabel: "x label", ylabel: "y label",
current_graph: {}}

export const userSlice = createSlice({
    name: "scatterplot",
    initialState: {value: initialStates},
    reducers: {
        forminput: (state, action) => {
            state.value = action.payload
            /*switch (action.type) {
                case "ALL":
                    return void(state.value = action.payload);
                case "MERGED":
                    return state.value = action.payload;
                default:
                    return state.value = action.payload;
            }*/
        },
    },
});

export const { forminput } = userSlice.actions;

export default userSlice.reducer;

