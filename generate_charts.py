import pandas as pd
import numpy as np
import os
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt


def save_fig_if_not_exists(file_path: str):
    file_path = Path(file_path)
    if not file_path.exists():
        plt.savefig(file_path)


def main():
    """Main function"""

    os.makedirs('charts', exist_ok=True)
    sns.set()
    sns.set_style('whitegrid')
    survey_data = pd.read_csv('survey.csv')

    # Faculty distribution
    plt.figure(figsize=(18, 6))
    plt.title(r'$\bf{Faculty\ Distribution}$')
    plt.subplots_adjust(bottom=0.20)
    faculty_counts = survey_data['faculty'].value_counts()
    sns.barplot(x=faculty_counts.index, y=faculty_counts.values)
    plt.xticks(rotation=10)
    plt.xlabel(r'$\bf{Faculty}$')
    plt.ylabel(r'$\bf{Number\ of\ Students}$')
    save_fig_if_not_exists('charts/faculty_distribution.png')
    plt.clf()

    # Year of study distribution
    year_counts = survey_data['year'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=year_counts.index, y=year_counts.values)
    plt.xlabel(r'$\bf{Year\ of\ Study}$')
    plt.ylabel(r'$\bf{Number\ of\ Students}$')
    plt.title(r'$\bf{Year\ of\ Study\ Distribution}$')
    save_fig_if_not_exists('charts/year_of_study_distribution.png')
    plt.clf()

    # cGPA distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data=survey_data, x='gpa_range')
    plt.xlabel(r'$\bf{cGPA\ Range}$')
    plt.ylabel(r'$\bf{Frequency}$')
    plt.title(r'$\bf{cGPA\ Range\ Distribution}$')
    save_fig_if_not_exists('charts/cgpa_range_distribution.png')
    plt.clf()

    # Quality of ChatGPT
    plt.figure(figsize=(10, 6))
    sns.histplot(data=survey_data, x='rating')
    plt.xlabel(r'$\bf{Rating}$')
    plt.ylabel(r'$\bf{Frequency}$')
    plt.title(r'$\bf{ChatGPT\ Quality}$')
    save_fig_if_not_exists('charts/chatgpt_quality.png')
    plt.clf()

    colors = sns.color_palette('pastel')
    np.random.shuffle(colors)
    # ChatGPT for Ideas Pie Chart
    is_using_cgpt_for_ideas_cheating = survey_data['is_using_cgpt_for_ideas_cheating'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(is_using_cgpt_for_ideas_cheating.values, labels=is_using_cgpt_for_ideas_cheating.index, autopct='%1.1f%%',
            colors=colors)
    plt.title(r'$\bf{Is\ Using\ ChatGPT\ For\ Ideas\ Considered\ Cheating?}$')
    save_fig_if_not_exists('charts/chatgpt_for_ideas.png')
    plt.clf()

    # ChatGPT for Writing Pie Chart
    is_using_cgpt_to_write_cheating = survey_data['is_using_cgpt_to_write_cheating'].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(is_using_cgpt_to_write_cheating.values, labels=is_using_cgpt_to_write_cheating.index, autopct='%1.1f%%',
            colors=colors)
    plt.title(
        r'$\bf{Is\ Using\ ChatGPT\ For\ Writing}$' + '\n' + r'$\bf{Code/Essay/Assignments\ Considered\ Cheating?}$')
    save_fig_if_not_exists('charts/chatgpt_for_writing.png')
    plt.clf()

    # Will ChatGPT increase plagiarism/cheating
    will_cgpt_increase_cheating = survey_data['will_cgpt_increase_cheating'].value_counts()
    plt.figure(figsize=(9, 6))
    plt.pie(will_cgpt_increase_cheating.values, labels=will_cgpt_increase_cheating.index, autopct='%1.1f%%',
            colors=colors)
    plt.title(r'$\bf{Will\ ChatGPT\ Increase\ Plagiarism/Cheating?}$')

    save_fig_if_not_exists('charts/will_chatgpt_increase_plagiarism.png')
    plt.clf()

    # Will ChatGPT hinder learning
    will_cgpt_increase_or_hinder_learning = survey_data['will_cgpt_increase_or_hinder_learning'].value_counts()
    plt.figure(figsize=(9, 6))
    plt.pie(will_cgpt_increase_or_hinder_learning.values, labels=will_cgpt_increase_or_hinder_learning.index,
            autopct='%1.1f%%',
            colors=colors)
    plt.title(r'$\bf{Will\ ChatGPT\ Hinder\ Learning?}$')
    save_fig_if_not_exists('charts/will_chatgpt_hinder_learning.png')
    plt.clf()

    # How can universities handle use of ChatGPT
    how_can_unis_handle_cgpt = survey_data['how_can_unis_handle_cgpt'].value_counts()
    plt.figure(figsize=(13.8, 8))
    plt.pie(how_can_unis_handle_cgpt.values, labels=how_can_unis_handle_cgpt.index,
            autopct='%1.1f%%',
            colors=colors)
    plt.title(r'$\bf{How\ Can\ Universities\ Handle\ Use\ of\ ChatGPT?}$')
    save_fig_if_not_exists('charts/how_can_unis_handle_use_of_chatgpt.png')
    plt.clf()


if __name__ == '__main__':
    main()
