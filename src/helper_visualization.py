import matplotlib.pyplot as plt
import numpy as np

def hist_by_labels(df, column_name, top=None, log=False, horizontal=True, left=None, right=None):
    """
    The `hist_by_labels` function creates a histogram plot of the distribution of values in a specified
    column of a DataFrame, with options for limiting the number of top values shown, using a log scale,
    and choosing the orientation of the plot.
    
    :param df: The dataframe containing the data
    :param column_name: The name of the column in the DataFrame for which you want to create a histogram
    :param top: The "top" parameter specifies the number of top values to include in the histogram. If
    it is set to None, all unique values in the specified column will be included. If a number is
    provided, only the top "n" values will be included in the histogram
    :param log: The `log` parameter determines whether the y-axis of the histogram should be displayed
    on a logarithmic scale. By default, it is set to `False`, meaning the y-axis will be displayed on a
    linear scale. If you set `log=True`, the y-axis will be displayed on a logarith, defaults to False
    (optional)
    :param horizontal: The `horizontal` parameter determines whether the histogram will be plotted
    horizontally (`True`) or vertically (`False`), defaults to True (optional)
    """
    
    # Calculate value counts for the specified column
    if top == None:
        value_counts = df[column_name].value_counts()
    else:
        value_counts = df[column_name].value_counts().head(top)

    # Create a wider or taller histogram plot depending on the orientation
    figsize = (len(value_counts)//2, 8) if horizontal else (12, len(value_counts)//2)
    plt.figure(figsize=figsize)
    
    
    # Choose the appropriate bar plot function based on orientation and log scale
    plot_func = plt.bar if horizontal else plt.barh
    
    # Plot the data with or without a log scale
    bars = plot_func(value_counts.index, value_counts.values, log=log, color='green')
    
    # # Set plot titles and labels
    if not horizontal:
        plt.gca().invert_yaxis()  # Invert y-axis if horizontal
    
    plt.title(f'{column_name} Distribution (Log Scale)' if log else f'{column_name} Distribution')
    plt.xlabel(column_name)
    plt.ylabel('Count (Log Scale)' if log else 'Count')
    
    # plot a red dash line at the left
    if left is not None and horizontal:
        plt.axvline(x=left, color='red', linestyle='--')
    # plot a red line at the right
    if right is not None and horizontal:
        plt.axvline(x=right, color='red', linestyle='--')
    
    # Add white-colored numbers in the middle of each bar
    for bar in bars:
        if horizontal:
            height = bar.get_height()
            text_x = bar.get_x() + bar.get_width() / 2
            text_y = height * 0.9
            plt.text(text_x, text_y,
                f'{int(height)}',
                ha='center', va='center', rotation=90,
                fontsize=8, color='black')
        else:
            width = bar.get_width()
            text_x = bar.get_x() +  width
            text_y = bar.get_y() + bar.get_height() / 2         
            plt.text(text_x, text_y,
                f'{int(width)}',
                ha='center', va='center', rotation=0,
                fontsize=8, color='black')
        # print(text_x, text_y)
    if horizontal:
        plt.xticks(rotation=90)

    plt.show()

def plot_history(history, title='', axs=None, exp_name=""):
    """
    The function `plot_history` is used to plot the loss and accuracy history of a model during training
    and validation.
    
    :param history: The `history` parameter is the history object returned by the `fit` method of a
    Keras model. It contains the training and validation metrics for each epoch
    :param title: The title of the plot. It is an optional parameter and can be left empty if not needed
    :param axs: The `axs` parameter is an optional argument that allows you to pass in a tuple of two
    `matplotlib` axes objects. If `axs` is provided, the function will use those axes to plot the loss
    and accuracy curves. If `axs` is not provided, the function will
    :param exp_name: The `exp_name` parameter is a string that represents the name of the experiment or
    model. It is used to label the lines in the plot with the corresponding experiment or model name
    :return: a tuple containing the two axes objects (ax1 and ax2) that were created for the subplots.
    """
    if axs is not None:
        ax1, ax2 = axs
    else:
        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    ax1.plot(history.history['loss'], label='train loss'  + exp_name)
    ax1.plot(history.history['val_loss'], label='val loss'  + exp_name)
    ax1.set_title('Loss')
    ax1.legend()
    
    ax2.plot(history.history['accuracy'], label='train accuracy'  + exp_name)
    ax2.plot(history.history['val_accuracy'], label='val accuracy'  + exp_name)
    ax2.set_title('Accuracy')
    ax2.legend()

    return (ax1, ax2)

# plot confusion matrix
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def plot_confusion_matrix(y_true, y_pred, labels=None, title='Confusion matrix', cmap=plt.cm.Blues):
    # Compute confusion matrix
    if labels is None:
        labels = np.unique(y_true)
    
    cm = confusion_matrix(y_true, y_pred, labels=labels, normalize='true')
    
    # get the diagonal values
    cm_diag = np.diag(cm)
    # sort the confusion matrix by class's name
    idx = np.argsort(cm_diag)[::-1]
    labels = labels[idx]
    cm = cm[idx][:, idx]
    
    fig, ax = plt.subplots(figsize=(12,12))
    sns.heatmap(cm, annot=True, fmt='.2f', ax=ax, cmap=plt.cm.Blues, cbar=False)
    # sns.heatmap(cm, annot=True, fmt='d', ax=ax, cmap=plt.cm.Blues, cbar=False)
    ax.set(xlabel="Pred", ylabel="True", title=title)
    ax.set_yticklabels(labels, rotation=0)
    ax.set_xticklabels(labels, rotation=90)
    plt.show()
    