#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Fr 21 Jul 2023 20:16:59 
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'grating'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/scholz_la/Desktop/grating_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "trial" ---
grating = visual.GratingStim(
    win=win, name='grating',
    tex='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1), sf=15.0, phase=1.0,
    color=[0,1,0], colorSpace='rgb',
    opacity=None, contrast=-1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=0.0)
grating_2 = visual.GratingStim(
    win=win, name='grating_2',
    tex='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1), sf=15.0, phase=1.0,
    color=[0,1,0], colorSpace='rgb',
    opacity=None, contrast=-1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
noise = visual.NoiseStim(
    win=win, name='noise',
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, 0), size=(2,2), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='White', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-2.0)
noise.buildNoise()

# --- Initialize components for Routine "trial" ---
grating = visual.GratingStim(
    win=win, name='grating',
    tex='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1), sf=15.0, phase=1.0,
    color=[0,1,0], colorSpace='rgb',
    opacity=None, contrast=-1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=0.0)
grating_2 = visual.GratingStim(
    win=win, name='grating_2',
    tex='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1), sf=15.0, phase=1.0,
    color=[0,1,0], colorSpace='rgb',
    opacity=None, contrast=-1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
noise = visual.NoiseStim(
    win=win, name='noise',
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, 0), size=(2,2), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='White', noiseElementSize=[0.0625], 
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-2.0)
noise.buildNoise()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "trial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [grating, grating_2, noise]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial" ---
while continueRoutine and routineTimer.getTime() < 45.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *grating* updates
    if grating.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
        # keep track of start time/frame for later
        grating.frameNStart = frameN  # exact frame index
        grating.tStart = t  # local t and not account for scr refresh
        grating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'grating.started')
        grating.setAutoDraw(True)
    if grating.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > grating.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            grating.tStop = t  # not accounting for scr refresh
            grating.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating.stopped')
            grating.setAutoDraw(False)
    if grating.status == STARTED:  # only update if drawing
        grating.setPhase(2*t, log=False)
    
    # *grating_2* updates
    if grating_2.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
        # keep track of start time/frame for later
        grating_2.frameNStart = frameN  # exact frame index
        grating_2.tStart = t  # local t and not account for scr refresh
        grating_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grating_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'grating_2.started')
        grating_2.setAutoDraw(True)
    if grating_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > grating_2.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            grating_2.tStop = t  # not accounting for scr refresh
            grating_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating_2.stopped')
            grating_2.setAutoDraw(False)
    if grating_2.status == STARTED:  # only update if drawing
        grating_2.setPhase(-2*t, log=False)
    
    # *noise* updates
    if noise.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        noise.frameNStart = frameN  # exact frame index
        noise.tStart = t  # local t and not account for scr refresh
        noise.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'noise.started')
        noise.setAutoDraw(True)
    if noise.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > noise.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            noise.tStop = t  # not accounting for scr refresh
            noise.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'noise.stopped')
            noise.setAutoDraw(False)
    if noise.status == STARTED:
        if noise._needBuild:
            noise.buildNoise()
        else:
            if (frameN-noise.frameNStart) %     1==0:
                noise.updateNoise()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial" ---
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-45.000000)

# --- Prepare to start Routine "trial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [grating, grating_2, noise]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial" ---
while continueRoutine and routineTimer.getTime() < 45.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *grating* updates
    if grating.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
        # keep track of start time/frame for later
        grating.frameNStart = frameN  # exact frame index
        grating.tStart = t  # local t and not account for scr refresh
        grating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'grating.started')
        grating.setAutoDraw(True)
    if grating.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > grating.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            grating.tStop = t  # not accounting for scr refresh
            grating.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating.stopped')
            grating.setAutoDraw(False)
    if grating.status == STARTED:  # only update if drawing
        grating.setPhase(2*t, log=False)
    
    # *grating_2* updates
    if grating_2.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
        # keep track of start time/frame for later
        grating_2.frameNStart = frameN  # exact frame index
        grating_2.tStart = t  # local t and not account for scr refresh
        grating_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grating_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'grating_2.started')
        grating_2.setAutoDraw(True)
    if grating_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > grating_2.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            grating_2.tStop = t  # not accounting for scr refresh
            grating_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating_2.stopped')
            grating_2.setAutoDraw(False)
    if grating_2.status == STARTED:  # only update if drawing
        grating_2.setPhase(-2*t, log=False)
    
    # *noise* updates
    if noise.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        noise.frameNStart = frameN  # exact frame index
        noise.tStart = t  # local t and not account for scr refresh
        noise.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'noise.started')
        noise.setAutoDraw(True)
    if noise.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > noise.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            noise.tStop = t  # not accounting for scr refresh
            noise.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'noise.stopped')
            noise.setAutoDraw(False)
    if noise.status == STARTED:
        if noise._needBuild:
            noise.buildNoise()
        else:
            if (frameN-noise.frameNStart) %     1==0:
                noise.updateNoise()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial" ---
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-45.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
